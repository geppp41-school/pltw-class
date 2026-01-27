shader_type canvas_item;
uniform vec2 center = vec2(0.5,0.5);
uniform float radius = 0.12;
uniform vec4 circle_color : source_color = vec4(1.0, 0, 0, 1.0);
uniform vec4 bg_color : source_color = vec4(0.0, 0.0, 0.0, 0.0);
 
void vertex() {
	// Called for every vertex the material is visible on.
	
}

void fragment() {
	vec2 to_center = center - UV;
	float dist = sqrt(dot(to_center, to_center));
	
	if(dist < radius) {
		COLOR = COLOR;
	} else {
		COLOR = bg_color;
	}
}

//void light() {
//	// Called for every pixel for every light affecting the CanvasItem.
//	// Uncomment to replace the default light processing function with this one.
//}
