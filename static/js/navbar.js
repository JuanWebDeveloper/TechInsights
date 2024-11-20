const toggleNavigation = () => {
 const bars = document.querySelector('.bars');
 const navigation = document.querySelector('.navigation');

 if (navigation.classList.contains('active')) {
  bars.classList.remove('active');
  navigation.classList.remove('active');
 } else {
  bars.classList.add('active');
  navigation.classList.add('active');
 }
};

document.querySelector('.bars').addEventListener('click', () => toggleNavigation());
