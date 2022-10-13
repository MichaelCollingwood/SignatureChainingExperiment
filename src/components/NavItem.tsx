import Link from 'next/link';
import Emoji from './Emoji';

export default function NavItem({emoji, label}: {emoji: string, label: string}) {
    return (
        <div className="px-1">
            <li className="sm:inline-flex sm:w-auto w-full px-3 py-2 rounded bg-black hover:bg-white text-white font-bold hover:text-black">
                <Link href='/'>
                    <div>
                        <Emoji symbol={emoji} label={label}/>
                        <h1 className="inline-flex">{label}</h1>
                    </div>
                </Link>
            </li>
        </div>
    )
}