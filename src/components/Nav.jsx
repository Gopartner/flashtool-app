import React, { useState } from 'react';
import navItemData from '../data/nav-item.json';

const Dropdown = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleDropdownClick = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="relative inline-block">
      <button onClick={handleDropdownClick} className="text-blue-500 hover:text-blue-700 focus:outline-none">
        Pilihan
      </button>
      {/* Tambahkan konten dropdown di sini */}
      {/* Konten akan ditampilkan jika state isOpen bernilai true */}
      {isOpen && (
        <div className="absolute bg-white shadow-md rounded-md p-2 mt-1 w-48">
          <a href="#" className="block py-1 px-4 text-gray-800 hover:bg-gray-200">File 1</a>
          <a href="#" className="block py-1 px-4 text-gray-800 hover:bg-gray-200">File 2</a>
          <a href="#" className="block py-1 px-4 text-gray-800 hover:bg-gray-200">File 3</a>
          {/* Tambahkan lebih banyak item berkas TWRP.img di sini */}
        </div>
      )}
    </div>
  );
}

const Nav = () => {
  return (
    <nav className="bg-gray-200 p-4">
      <ul className="flex justify-center space-x-4">
        {navItemData.map((item, index) => (
          <li key={index}>
            {/* Gunakan dropdown */}
            <Dropdown />
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Nav;

