module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors:{
        brand: {
          red: {
            light: {
              1: "#F7F3F2",
              2: '#F2EBE9'
            },           
            dark: "#E7332B"
          },
          gray: {
            dark: {
              1: '#514949',
              2: '#898989',
            },
            light: {
              1: "#A08F8F",
              2: "#E5E5E5"
            },
            blue: '#4774E8'
          }
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
