<template>
    <div id="navbar">
        <img src="./assets/logo.png" alt="logo">
        <h2>YDL</h2>
    </div>
</template>

<script>
export default {
    name: 'navbar'
}
</script>

<style lang="scss" scoped>
#navbar {
    display: block;
    background-color: #343434;
    padding: 10px;
    padding-bottom: 7px;
    text-align: left;

    img {
        display: inline-block;
        width: 50px;
        margin-left: 50px;
    }

    h2 {
        display: inline-block;
        line-height: 35px;
        vertical-align: top;
        color: #ffffff;
        margin: 0px;
        margin-left: 3px;
        font-size: 23px;
        font-weight: bold;
        font-family: NotoSansCondensed;
    }
}
</style>