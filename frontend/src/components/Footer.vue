<template>
    <div class="max-w-7xl mx-auto my-6 py-16 px-6 text-brand-gray-dark-1">
        <div class="md:flex md:justify-between mb-16 py-4 text-center md:text-left font-medium">
            <div class="mb-8 md:mb-0 text-3xl md:text-2xl font-bold">
                <router-link to="/" class="hover:text-brand-red-dark">Zuri<span class="text-brand-red-dark">.</span>Team</router-link>
            </div>
            <div class="mb-8 md:mb-0">
                <h2 class="mb-3 font-bold text-2xl md:text-base">Links</h2>
                <ul class="font-medium text-brand-red-dark">
                    <li class="mb-3"><a href="flutterwave.com/store/zuriteam">Store</a></li>
                    <li class="mb-3"><a href="blog.zuri.team">Blog</a></li>
                </ul>
            </div>
            <div class="mb-8 md:mb-0">
                <h2 class="mb-3 font-bold text-2xl md:text-base">Contact</h2>
                <div class="mb-3 text-sm">
                    <p>8 Jubllie-CMD Road, Magodo,</p>
                    <p>Lagos State</p>
                </div>
                <div class="text-sm">
                    <a class="text-brand-red-dark" href="mailto:hello@zuri.com">hello@zuri.com</a>
                </div>
            </div>
            <div>
                <h2 class="mb-3 font-bold text-2xl md:text-base">Follow Us</h2>
                <div class="flex justify-center space-x-2">
                    <div><a href="https://web.facebook.com/thezuriteam"><img class="w-5" src="../assets/facebook.png" alt="Facebook Logo"></a></div>
                    <div><a href="https://twitter.com/theZuriTeam"><img class="w-5" src="../assets/twitter.png" alt="Twitter Logo"></a></div>
                    <div><a href="https://www.instagram.com/thezuriteam"><img class="w-5" src="../assets/instagram.png" alt="Instagram Logo"></a></div>
                    <div><a href="https://www.linkedin.com/company/zuri-team"><img class="w-5" src="../assets/linkedin.png" alt="LinkedIn Logo"></a></div>
                </div>
            </div>
        </div>
        <div class="my-3 border-t-2 border-brand-gray-light-1"></div>
        <div class="py-4 my-1 font-bold text-center">&copy; 2021 ZURI TEAM</div>
    </div>
</template>

<script>
export default {
name: 'Footer'
}
</script>
