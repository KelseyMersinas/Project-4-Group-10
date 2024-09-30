var viz;

$(document).ready(function() {
    initializeViz();

    $("#pdf").click(function() {
        exportPDF();
    });
    $("#image").click(function() {
        exportImage();
    });
    $("#crosstab").click(function() {
        exportCrossTab();
    });
    $("#data").click(function() {
        exportData();
    });
    $("#revert").click(function() {
        revertAll();
    });
});

function initializeViz() {
    var placeholderDiv = document.getElementById("tableauViz");
    var url = "https://public.tableau.com/views/HalloweenCandyApril2022/Story1";
    var options = {
        width: placeholderDiv.offsetWidth,
        height: placeholderDiv.offsetHeight,
        hideTabs: true,
        hideToolbar: true,
        onFirstInteractive: function() {
            workbook = viz.getWorkbook();
            activeSheet = workbook.getActiveSheet();
        }
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
}