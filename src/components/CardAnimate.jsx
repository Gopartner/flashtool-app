import React from 'react';
import { useSpring, animated } from 'react-spring';

const CardAnimate = ({ children }) => {
  const [flipped, setFlipped] = React.useState(false);

  const springProps = useSpring({
    transform: `perspective(600px) rotateX(${flipped ? 180 : 0}deg)`,
    config: { mass: 5, tension: 500, friction: 80 },
  });

  const handleClick = () => {
    setFlipped(!flipped);
  };

  return (
    <animated.div
      className="relative w-64 h-64"
      style={{
        ...springProps,
        overflow: 'hidden',
      }}
    >
      <animated.div
        className="absolute top-0 left-0 w-full h-full bg-white shadow-md rounded p-6 cursor-pointer"
        onClick={handleClick}
        style={{
          backfaceVisibility: 'hidden',
          transform: springProps.transform.interpolate(t => `${t} rotateX(180deg)`),
        }}
      >
        {children}
      </animated.div>
    </animated.div>
  );
};

export default CardAnimate;

