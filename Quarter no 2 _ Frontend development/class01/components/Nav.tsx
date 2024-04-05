import Link from "next/link";
// import Card from "./Card";
const Nav = () => {
    return (
        
        <div>
                <p>Create a component for navbar</p>
      
            <ul>
                <li><Link href="/">Home</Link></li>
                <li><Link href="/About">About</Link></li>
                <li><Link href="/Products">Products</Link></li>
               
            </ul>
        </div>
    
    );
}

export default Nav;
