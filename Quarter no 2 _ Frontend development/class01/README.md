## Next.js14 start:

### step1:To make project folder: 
- npx create-next-app@latest

### step2:To run project: 
- npm run dev 

### step3: pakage.json file change:
- "autoprefixer": "10.0.1",  // remove hat from start 

### how we make route in next.js?
 - step1: create folder (route name _ and start with capital letter) in app folder 
 - and then make file (page.tsx) in this route folder 

 ### Navigation in next.js?
follow this syntax
 - import Link from "next/link";
 - <li><Link href="/">Home</Link></li>

### How we create Component?
- create a folder in main structure called "Component"
- and make component name file e.g (Card.tsx) and then call "<Card/>"

## Dynamic routes and static routes 

### Static Routes:

- Purpose: Serve content that remains the same for all users.
- Usage: Ideal for pages with fixed content or information that doesn't change frequently.
- Benefit: Pre-rendered at build time for efficiency and SEO optimization.
- syntax: Create a file in the pages directory with the desired route structure (e.g., about.js for /about).

### Dynamic Routes:

- Purpose: Generate pages with URLs dependent on external data or user input.
- Usage: Suitable for creating pages with variable content or generating pages dynamically based on parameters in the URL.
- Benefit: Enables building dynamic web applications with personalized content and flexible routing
- syntax: Use square brackets [] in the file name to indicate dynamic segments in the URL (e.g., [slug].js for /blog/[slug]).
- Create the file inside a directory named after the dynamic route (e.g., blog/[slug].js).
- Each file in the dynamic route directory represents a unique page for different dynamic values.
