import React from 'react';
import headerData from '../data/header.json';
import ProfilImage from './ProfilImage';

const Header = () => {
  return (
    <header className="bg-blue-500 text-white text-center p-4">
    <ProfilImage />
      <h1 className="text-2xl font-bold">{headerData.title}</h1>
      <p className="text-sm">{headerData.description}</p>
    </header>
  );
}

export default Header;

