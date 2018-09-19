<template>
    <div>
        <input type="text" name="password" id="password" ref="password">
        <input type="text" v-validate="'confirmed:password'" name="passwordConfirm" id="passwordConfirm" ref="passwordConfirm">
        <span>{{ errors.first('passwordConfirm') }}</span>
    </div>
</template>


