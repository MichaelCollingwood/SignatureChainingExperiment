import React from 'react';
import { Header } from '../components/Head';
import { Navbar } from '../components/NavBar';

export default function Home() {
  return (
    <div>
      <Header />
      <Navbar />
      <div className='bg-slate-200 p-2'>
        Info
      </div>
    </div>
  );
}