import React, { useState, useEffect } from 'react';
import { useSpring, animated } from 'react-spring';
import SetStyleModal from './SetStyleModal'; // Import komponen modal

const AnimatedButton = () => {
  const [hovered, setHovered] = useState(false);
  const [showMenu, setShowMenu] = useState(false);
  const [settings, setSettings] = useState({
    backgroundColor: 'bg-blue-500',
    textColor: 'text-white',
    fontSize: 'text-base',
    position: 'mx-0',
  });

  const { scale } = useSpring({
    to: { scale: hovered ? 1.2 : 1 },
    config: { tension: 300, friction: 10 },
  });

  // Load settings from JSON file
  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const response = await fetch('../data/set-style-button.json'); // Ganti path sesuai dengan lokasi file
        const data = await response.json();
        setSettings(data);
      } catch (error) {
        console.error('Error fetching settings:', error);
      }
    };

    fetchSettings();
  }, []);

  const toggleMenu = () => {
    setShowMenu(!showMenu); // Mengubah nilai showMenu saat tombol diklik
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setSettings({ ...settings, [name]: value });
  };

  return (
    <div>
      <animated.button
        className={`${settings.backgroundColor} ${settings.textColor} font-bold py-2 px-4 rounded ${settings.position} w-full mb-2`}
        style={{ transform: scale.interpolate(s => `scale(${s})`) }}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        onClick={toggleMenu}
      >
        Setting bro
      </animated.button>
      <SetStyleModal
        isOpen={showMenu} // Menggunakan nilai showMenu untuk menentukan apakah modal ditampilkan
        onRequestClose={toggleMenu} // Menggunakan toggleMenu sebagai event handler untuk menutup modal
        settings={settings}
        onChange={handleChange}
      />
    </div>
  );
};

export default AnimatedButton;

