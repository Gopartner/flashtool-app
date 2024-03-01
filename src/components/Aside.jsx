import React from 'react';
import asideData from '../data/aside.json';

const Aside = () => {
  return (
    <aside className="p-4 bg-gray-100">
      <p>{asideData.content}</p>
    </aside>
  );
}

export default Aside;

