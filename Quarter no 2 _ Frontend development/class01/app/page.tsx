// import Link from "next/link";
import Card from "@/components/Card";
import Nav from "@/components/Nav";

export default function Home(){
    return(
        <>
        <h1> landing page is here</h1>

        {/* <ul>
            <li><Link href="/">Home</Link></li>
            <li><Link href="/About">About</Link></li>
            <li><Link href="/Products">Products</Link></li>
        </ul> */}
        <Nav/>
        <Card/>
        <Card/>
        </>
    )
}
