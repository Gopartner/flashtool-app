// Main.jsx
import React from 'react';
import Article from './Article';
import Aside from './Aside';
import AnimateButton from './AnimateButton';

const Main = () => {
  return (
    <>
    <AnimateButton />
    <main className="flex-grow flex justify-center">
      <div className="max-w-2xl w-full">
        <Article />
        <Aside />
      </div>
    </main>
    </>
  );
}

export default Main;

