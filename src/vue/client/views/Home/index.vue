<template>
    <div>
        <h2 class="title">{{ title }}</h2>
        <div class="content">
            {{ content }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            title: 'We are VGU Alumni',
            content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`,
        };
    }
}
</script>

