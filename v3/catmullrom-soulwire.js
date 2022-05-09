// From http://jsfiddle.net/soulwire/HbMLh/

function catmullRom( points, ctx ) {
    
    var p0, p1, p2, p3, i6 = 1.0 / 6.0;
    
    for ( var i = 3, n = points.length; i < n; i++ ) {

        p0 = points[i - 3];
        p1 = points[i - 2];
        p2 = points[i - 1];
        p3 = points[i];
        
        ctx.bezierCurveTo(
            p2.x * i6 + p1.x - p0.x * i6,
            p2.y * i6 + p1.y - p0.y * i6,
            p3.x * -i6 + p2.x + p1.x * i6,
            p3.y * -i6 + p2.y + p1.y * i6,
            p2.x,
            p2.y
        );
    }
}

var MAX_POINTS = 100;
var MIN_DISTANCE = 20;

var points = [];
var point = { x: 0, y: 0 };

Sketch.create({
    
    draw: function() {
        
        // Draw points
        
        this.globalAlpha = 0.1;

        for ( var i = 0; i < points.length; i++ ) {
            this.beginPath();
            this.arc( points[i].x, points[i].y, 5, 0, TWO_PI );
            this.fill();
        }
        
        // Draw curve
        
        this.globalAlpha = 0.8;
        this.beginPath();
        catmullRom( points, this );
        this.stroke();
    },

    mousemove: function() {

        if ( this.dragging ) {

            if ( points.length > MAX_POINTS ) points.shift();
            
            var dx = this.mouse.x - point.x;
            var dy = this.mouse.y - point.y;
            
            if ( sqrt( dx*dx + dy*dy ) > MIN_DISTANCE ) {
                
                point = {
                    x: this.mouse.x,
                    y: this.mouse.y
                };
                
                points.push( point );
            }
        }
    }
});
