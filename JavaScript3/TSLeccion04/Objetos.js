let persona = {
	nombre = 'Lucas',
	apellido = 'Lavena',
	edad = 25,
	email = 'lucaslavena999@gmail.com',
	function nombreCompleto() {
		return this.nombre+' '+this.apellido;
	}
}
console.log(persona.nombreCompleto())

let persona2 = new Object();
persona2.nombre = 'Juan';
persona2.apellido = 'Lorenzo';
persona2.edad = 23;
persona2.email = 'yo@hotmail.com.ar';

console.log(persona2);
