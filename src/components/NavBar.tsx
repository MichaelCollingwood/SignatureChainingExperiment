import Link from 'next/link';
import { useState } from 'react';
import Emoji from './Emoji'
import Title from './Title'

export const Navbar = () => {
    const [active, setActive] = useState(false);

    const handleClick = () => {
        setActive(!active);
    };

    return (
        <section className="bg-turner">
            <nav className='flex items-center flex-wrap p-2 '>
                <Link href='/'>
                <a className='inline-flex items-center p-2 pl-4 mr-4 '>
                    <Title />
                </a>
                </Link>
                <button
                className=' inline-flex p-3 hover:bg-white rounded sm:hidden text-white ml-auto hover:text-white outline-none'
                onClick={handleClick}
                >
                    <svg
                        className='w-6 h-6'
                        fill='none'
                        stroke='black'
                        viewBox='0 0 24 24'
                        xmlns='http://www.w3.org/2000/svg'
                    >
                        <path
                        strokeLinecap='round'
                        strokeLinejoin='round'
                        strokeWidth={2}
                        d='M4 6h16M4 12h16M4 18h16'
                        />
                    </svg>
                </button>
                {/*Note that in this div we will use a ternary operator to decide whether or not to display the content of the div  */}
                <div
                className={`${
                    active ? '' : 'hidden'
                } w-full sm:inline-flex sm:flex-grow sm:w-auto`}
                >
                    <ul className='sm:inline-flex sm:flex-row sm:ml-auto sm:w-auto w-full sm:items-center items-start  flex flex-col sm:h-auto'>
                        <li className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold hover:bg-white hover:text-white">
                            <button id="dropdownNavbarLink" data-dropdown-toggle="dropdownNavbar">
                                <Emoji symbol="🌍" label="home"/>
                            </button>
                            <div id="dropdownNavbar" className="hidden z-10 w-44 font-normal bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600">
                                <ul className="py-1 text-sm text-gray-700 dark:text-gray-400" aria-labelledby="dropdownLargeButton">
                                    <li>
                                        <Link href='/'>
                                            <a href="#" className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold items-center justify-center hover:bg-white hover:text-white">
                                                Dashboard
                                            </a>
                                        </Link>
                                    </li>
                                    <li>
                                        <Link href='/'>
                                            <a href="#" className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold items-center justify-center hover:bg-white hover:text-white">
                                                Settings
                                            </a>
                                        </Link>
                                    </li>
                                    <li>
                                        <Link href='/'>
                                            <a href="#" className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold items-center justify-center hover:bg-white hover:text-white">
                                                Earnings
                                            </a>
                                        </Link>
                                    </li>
                                </ul>
                                <div className="py-1">
                                    <Link href='/'>
                                        <a href="#" className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold items-center justify-center hover:bg-white hover:text-white">
                                            Sign out
                                        </a>
                                    </Link>
                                </div>
                            </div>
                        </li>
                        <li className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold hover:bg-white hover:text-white">
                            <Link href='/'>
                                <div>
                                    <Emoji symbol="👥" label="us"/>
                                </div>
                            </Link>
                        </li>
                        <li className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded text-white font-bold hover:bg-white hover:text-white">
                            <Link href='/'>
                                <Emoji symbol="📞" label="contact"/>
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </section>
    );
};
