import React from 'react';
import Header from './components/Header';
import Nav from './components/Nav';
import Main from './components/Main';
import Footer from './components/Footer';
//import AnimateButton from './components/AnimateButton';

const App = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <Nav />
      <div className="container mx-auto">
        <Main />
      </div>
      <Footer />
    </div>
  );
}

export default App;

