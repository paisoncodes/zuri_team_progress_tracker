<template>
    <div class="max-w-7xl mx-auto py-16 px-6 xl:px-0 text-brand-gray-dark-1 text-sm md:text-base">
        <div class="grid gap-x-3 grid-cols-2 md:grid-cols-3 lg:flex lg:justify-between">
            <div class="mb-10 lg:mb-0 text-lg md:text-2xl font-medium text-left order-last lg:order-first">
                <router-link to="/" class="hover:text-brand-red-dark">ZURI.TEAM</router-link>
            </div>
            <div class="mb-10 lg:mb-0">
                <h2 class="mb-6 text-lg md:text-2xl font-medium">Quick Links</h2>
                <ul>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Home</a></li>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Curriculum</a></li>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">FAQ</a></li>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Terms and Conditions</a></li>
                </ul>
            </div>
            <div class="mb-10 lg:mb-0">
                <h2 class="mb-6 text-lg md:text-2xl font-medium">Connect with us</h2>
                <ul>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Email</a></li>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Blog</a></li>
                    <li class="mb-1 md:mb-4"><a class="hover:text-brand-red-dark" href="">Store</a></li>
                </ul>
            </div>
            <div class="mb-10 lg:mb-0">
                <h2 class="mb-6 text-lg md:text-2xl font-medium">Office Address</h2>
                <p>8 Jubllie-CMD Road,</p>
                <p>Magodo, Lagos State</p>
            </div>
            <div class="mb-10">
                <h2 class="mb-6 text-lg md:text-2xl font-medium text-left lg:text-right">Follow us</h2>
                <div class="flex flex-1 lg:justify-between space-x-2 lg:space-x-4">
                    <div><a href="https://www.instagram.com/thezuriteam/?hl=en"><img src="../assets/instagram.png" alt="Instagram Logo"></a></div>
                    <div><a href="https://web.facebook.com/thezuriteam/?_rdc=1&_rdr"><img src="../assets/facebook.png" alt="Facebook Logo"></a></div>
                    <div><a href="https://www.linkedin.com/company/zuri-team"><img src="../assets/linkedin.png" alt="LinkedIn Logo"></a></div>
                    <div><a href="https://twitter.com/thezuriteam?lang=en"><img src="../assets/twitter.png" alt="Twitter Logo"></a></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
name: 'Footer'
}
</script>
