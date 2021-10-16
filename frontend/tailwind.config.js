module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      outline: {
        black: '1px solid #514949',
      },
      colors:{
        brand: {
          red: {
            light: {
              1: "#F7F3F2",
              2: '#F2EBE9',
              3: '#EDE2E2'
            },           
            dark: "#E7332B"
          },
          gray: {
            dark: {
              1: '#514949',
              2: '#898989',
              3: '#CFC4C1',
            },
            light: '#A08F8F',
            blue: '#4774E8'
          }
        },
      },
      screens: {
        xs: '475px'
      },
      fontFamily: {
        'mulish': ['Mulish', 'sans-serif'],
        'poppins': ['Poppins', 'sans-serif']
      },
      fontSize: {
        'md': '2rem',
        },
      height: {
        'pth': '39.8rem',
        },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
