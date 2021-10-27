<template>
    <div class="max-w-7xl mx-auto pb-16 pt-8 lg:px-6 xl:px-0 text-brand-gray-dark-1">
        <div class="md:grid md:grid-cols-3 lg:flex lg:justify-between lg:space-x-3 text-xs">
            <div class="mb-8 lg:mb-0 text-xl text-center lg:text-left">
                <router-link to="/" class="hover:text-brand-gray-light">ZURI.TEAM</router-link>
            </div>
            <div class="mb-10 lg:mb-0 text-center lg:text-left">
                <h2 class="mb-2 text-xl">Quick Links</h2>
                <ul>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Home</a></li>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Curriculum</a></li>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">FAQ</a></li>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Terms and Conditions</a></li>
                </ul>
            </div>
            <div class="mb-10 lg:mb-0 text-center lg:text-left">
                <h2 class="mb-2 text-xl">Connect with us</h2>
                <ul>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Email</a></li>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Blog</a></li>
                    <li class="mb-2"><a class="hover:text-brand-gray-light" href="">Store</a></li>
                </ul>
            </div>
            <div class="mb-10 lg:mb-0 text-center lg:text-left">
                <h2 class="mb-2 text-xl">Office Address</h2>
                <p>8 Jubllie-CMD Road,</p>
                <p>Magodo, Lagos State</p>
            </div>
            <div class="mb-10">
                <h2 class="mb-2 text-xl text-center lg:text-right">Follow us</h2>
                <div class="flex flex-1 justify-center lg:justify-between space-x-2 lg:space-x-6">
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
