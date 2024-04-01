class ImgLabeler{

    constructor(container_id, image_id) {
        this.container_id = container_id;
        this.image_id = image_id;
  
    }

    draw_table_header() {
        let html = '<thead>'
        html += '<tr>'
        html += '<th scope="col">KeyPoint</th>'
        html += '<th scope="col">X Coordinate</th>'
        html += '<th scope="col">Y Coordinate</th>'
        html += '<th scope="col">Value</th>'
        html += '</tr>'
        html += '</thead>'
        
        return html
    }

    draw_body() {
        let body= '<tbody>'
        body += '<tr>'
        body += '<td scope="row">Darts</th>'
        body += '<td>200</td>'
        body += '<td>400</td>'
        body += '<td>Coordinate Point Top</td>'
        body += '</tr>'
        body += '</tbody>'
        return body;

    }

    draw_footer() {
        let footer = '<tfoot>'
        footer += '<tr>'
        footer += '<button>Add</button>'
        footer += '</tr>'
        footer += '</tfoot>'

        return footer
    }

    draw_table() {

        $('#' + this.container_id).empty();

        let table = '<table class="table table-dark">'
        table += this.draw_table_header()
        table += this.draw_body()
        table += this.draw_footer()
        table += '</table>'
        $('#' + this.container_id).append(table)
    }

    build() {
        $('#' + this.container_id).empty();
        this.draw_table();

    }


}