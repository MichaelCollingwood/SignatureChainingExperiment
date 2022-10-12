import Head from 'next/head';
import React from 'react';
import { Navbar } from '../components/NavBar';
import { Map } from '../components/Map';

export default function Home() {
  

  return (
    <div>
      <Head>
        <title>6°</title>
      </Head>
      <Navbar />
      <Map />
    </div>
  );
}