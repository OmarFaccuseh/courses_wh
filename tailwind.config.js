/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html, js}"],
  theme: {
    extend: {
      colors: {
        semidark: '#2b2f44',
        green_light : '#e0f4f0',
        green_middle : '#a1e2db',
        green_semi_strong : '#8ea196',
        green_strong : '#14b8a6',
        green_super_strong : '#14b8a6',
      },
      boxShadow: {
        'solid': '-10px 10px 0px  #a1e2db', 
        'title': '-7px 7px 0px  #a1e2db', 
        'imagen': '11px 11px 0px  #8ea196', 
      },
    },
  },
  plugins: [],
}

