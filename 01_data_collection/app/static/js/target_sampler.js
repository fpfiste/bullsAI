class TargetSampler{

    constructor(container_id) {
        this.container_id = container_id;
  
    }

    
    get_dimensions(){
        this.parent_width = $(this.container_id).width()
        this.parent_height = $(this.container_id).height()
        this.canvas_dim = Math.min(this.parent_width, this.parent_height)
        this.margin_top = this.parent_height - this.canvas_dim
        this.margin_left = (this.parent_width - this.canvas_dim) / 2
    }

    get_target() { 
        this.x_coor = 0;
        this.y_coor = 0;

        // get max distance
        var max_x_dist = Math.abs(this.x_coor - (this.canvas_dim / 2))
        var max_y_dist = this.y_coor
        var max_distance = Math.sqrt( max_x_dist*max_x_dist + max_y_dist*max_y_dist );

        // initlize distance bigger than max distance
        let actual_distance = max_distance + 1

        // sample x and y coordinates until they are in range
        while ( actual_distance >= max_distance) {
            this.x_coor = Math.floor(Math.random() * (this.canvas_dim - 0 + 1) );
            this.y_coor = Math.floor(Math.random() * (this.canvas_dim - 0 + 1) );
            
            
            // get actual distance
            let actual_x_dist = Math.abs(this.x_coor - (this.canvas_dim / 2))
            let actual_y_dist = Math.abs(this.y_coor - (this.canvas_dim / 2))
            actual_distance = Math.sqrt( actual_x_dist*actual_x_dist + actual_y_dist*actual_y_dist );
          } 
    }

    draw_board() {
        let board_html = '<img id="target-board" src="/static/dartboard.jpg" width='+this.canvas_dim+' height='+this.canvas_dim+' style="margin-top:'+this.margin_top+'px; margin-left:'+this.margin_left+'px; border-radius: 50%;">'
        return board_html
    }

    draw_dot() {

        this.get_target();

        let target_html = '<span style="height: 15px; width: 15px; background-color:orange; border-radius: 50%; position:absolute; margin-left:'+this.x_coor+'px; margin-top: '+this.y_coor+'px;"></span>'

        return target_html
    }

    build() {

        this.get_dimensions();
        $(this.container_id).empty()

        let html = '<div id="target" style="display:flex;">'
        html += this.draw_board()
        html += this.draw_dot()
        html += '</div>'


      
        $(this.container_id).append(html)
        

    }

}