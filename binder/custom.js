function run() {
	document.getElementById('run_all_cells').click();
}
setTimeout(run, 1000);
var cells = document.getElementsByClassName('code_cell');
//*
for (var i = 0; i < cells.length - 1; i ++) {
	//cells[i].style.visibility = "hidden";
	cells[i].style.display='none';
}
cells[cells.length-1].firstChild.style.display='none';
function getLesson(me) {
	alert('1');
    var kernel = IPython.notebook.kernel;
    kernel.execute('myStr = ' + me.value);
}
