import React, { useState } from 'react';
import { animated, useSpring } from 'react-spring';

const Card = () => {
  const [flipped, setFlipped] = useState(false);

  const { transform, opacity } = useSpring({
    opacity: flipped ? 1 : 0,
    transform: `perspective(600px) rotateX(${flipped ? 180 : 0}deg)`,
    config: { mass: 5, tension: 500, friction: 80 },
  });

  const handleClick = () => {
    setFlipped(!flipped);
  };

  return (
    <animated.div
      className="bg-white shadow-md rounded p-6 w-64"
      style={{ opacity: opacity.interpolate(o => 1 - o), transform }}
      onClick={handleClick}
    >
      <div className="backface-hidden">
        <h1 className="text-lg font-bold mb-2">Card Title</h1>
        <p>Content goes here...</p>
      </div>
    </animated.div>
  );
};

export default Card;

