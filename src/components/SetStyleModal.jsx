import React from 'react';
import Modal from 'react-modal';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import settingsData from '../data/set-style-button.json'; // Impor data pengaturan awal

Modal.setAppElement('#root');

const SetStyleModal = ({ isOpen, onRequestClose }) => {
  const [settings, setSettings] = useState(settingsData); // State untuk menyimpan pengaturan

  const handleChange = (event) => {
    const { name, value } = event.target;
    setSettings({ ...settings, [name]: value }); // Mengubah pengaturan saat input diubah
  };

  const handleSave = () => {
    // Menyimpan pengaturan ke dalam berkas JSON
    localStorage.setItem('set-style-button', JSON.stringify(settings));
    
    // Terapkan pengaturan secara langsung di web
    document.documentElement.style.setProperty('--bg-color', settings.backgroundColor);
    document.documentElement.style.setProperty('--text-color', settings.textColor);
    document.documentElement.style.setProperty('--font-size', settings.fontSize);
    document.documentElement.style.setProperty('--position', settings.position);
    
    onRequestClose(); // Menutup modal setelah menyimpan pengaturan
  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onRequestClose}
      className="fixed inset-0 flex items-center justify-center"
      overlayClassName="bg-black bg-opacity-50"
    >
      <div className="bg-white rounded-lg shadow-lg p-4 max-w-md mx-auto">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-lg font-semibold">Settings</h2>
          <FontAwesomeIcon icon={faTimes} className="text-gray-600 cursor-pointer" onClick={onRequestClose} />
        </div>
        <div className="mb-4">
          <label className="block mb-2">
            Background Color:
            <input type="color" name="backgroundColor" value={settings.backgroundColor} onChange={handleChange} className="ml-2" />
          </label>
          <label className="block mb-2">
            Text Color:
            <input type="color" name="textColor" value={settings.textColor} onChange={handleChange} className="ml-2" />
          </label>
          <label className="block mb-2">
            Font Size:
            <select name="fontSize" value={settings.fontSize} onChange={handleChange} className="w-full p-2 border rounded-md ml-2">
              <option value="text-xs">Small</option>
              <option value="text-base">Medium</option>
              <option value="text-lg">Large</option>
            </select>
          </label>
          <label className="block mb-2">
            Position:
            <select name="position" value={settings.position} onChange={handleChange} className="w-full p-2 border rounded-md ml-2">
              <option value="mx-0">Center</option>
              <option value="ml-0">Left</option>
              <option value="mr-0">Right</option>
            </select>
          </label>
        </div>
        <div className="flex justify-end">
          <button onClick={handleSave} className="bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-700 mr-2">Save</button>
          <button onClick={onRequestClose} className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-700">Close</button>
        </div>
      </div>
    </Modal>
  );
};

export default SetStyleModal;

