import React from 'react';
import footerData from '../data/footer.json';

const Footer = () => {
  return (
    <footer className="bg-blue-500 text-white p-4">
      <p> {footerData.copyright}</p>
      <p>Email: {footerData.contact.email}</p>
      <p>Phone: {footerData.contact.phone}</p>
    </footer>
  );
}

export default Footer;

