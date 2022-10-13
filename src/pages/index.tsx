import Head from 'next/head';
import React from 'react';
import { Navbar } from '../components/NavBar';

export default function Home() {
  

  return (
    <div>
      <Head>
        <title>6°</title>
      </Head>
      <Navbar />
    </div>
  );
}