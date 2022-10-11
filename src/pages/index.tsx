import Head from 'next/head';
import { Navbar } from '../components/NavBar';
import SimpleMap from '../components/Map';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <Navbar />
      <div>
        <SimpleMap />
      </div>
    </div>
  );
}