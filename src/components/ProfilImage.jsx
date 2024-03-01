import React from 'react';
import logo from '../assets/images/logo-togelon.png'; // Path relatif menuju gambar profil

const ProfilImage = () => {
  return (
    <img src={logo} alt="Profil" className="w-40 h-10 rounded-full mx-auto mb-4" />
  );
}

export default ProfilImage;

