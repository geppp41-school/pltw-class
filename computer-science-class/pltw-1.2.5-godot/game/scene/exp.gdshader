shader_type canvas_item;

uniform float r = 1.0;
uniform float g = 0.0;
uniform float b = 0.0;
uniform float brightness = 0.8;
const vec4 edge_color = vec4(0.0, 0.0, 0.0, 1.0);


void vertex() {
	//if(COLOR == vec4(26.0/255.0, 26.0/255.0, 26.0/255.0, 1.0)){
		//COLOR = vec4(1.0, 0.0, 0.0, 1.0);
	//}
	// Called for every vertex the material is visible on.
}

void fragment() {
	float test = 204.0;
	if(COLOR.q ==1.0){
		if(round(COLOR.r*255.0) == 26.0 && round(COLOR.g*255.0) == 26.0 && round(COLOR.b*255.0) == 26.0){
			COLOR = vec4(0.3*r*brightness, 0.3*g*brightness, 0.3*b*brightness, 1.0);
		} else if(COLOR != edge_color) {
			COLOR = vec4((COLOR.r+0.1)*r*brightness, (COLOR.g+0.1)*g*brightness, (COLOR.b+0.1)*b*brightness, 1.0);
		}
		//if(round(COLOR.r*255.0) == test && round(COLOR.g*255.0) == test && round(COLOR.b*255.0) == test){
			//COLOR=vec4(0.0, 1.0, 0.0, 1.0);
		//}

	}
	//if(COLOR.r == test/255.0 && COLOR.g == test/255.0 && COLOR.b == test/255.0){
		//COLOR = vec4(0.0, 1.0, 0.0, 1.0);
	//}
	// Called for every pixel the material is visible on.
}

//void light() {
//	// Called for every pixel for every light affecting the CanvasItem.
//	// Uncomment to replace the default light processing function with this one.
//}
