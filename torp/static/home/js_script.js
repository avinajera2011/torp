function home() {
    document.getElementById("main_content").innerHTML = "<h1 style='text-align: left'>Operations research</h1><p></p> Operations research (British English: operational research), often shortened to the initialism OR, is a discipline that deals with the development and application of advanced analytical methods to improve decision-making. It is sometimes considered to be a subfield of mathematical sciences. The term management science is sometimes used as a synonym. Employing techniques from other mathematical sciences, such as modeling, statistics, and optimization, operations research arrives at optimal or near-optimal solutions to complex decision-making problems. Because of its emphasis on practical applications, operations research has overlap with many other disciplines, notably industrial engineering. Operations research is often concerned with determining the extreme values of some real-world objective: the maximum (of profit, performance, or yield) or minimum (of loss, risk, or cost). Originating in military efforts before World War II, its techniques have grown to concern problems in a variety of industries.</p>";
    document.getElementById("solvertool").style = "display: none";
    sessionStorage.setItem("button", 1);
}
function linprog()
{
    document.getElementById("main_content").innerHTML = "<h1 style='text-align: left'>Linear programming</h1><p >Linear programming (LP, also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (also known as mathematical optimization). More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. Its feasible region is a convex polytope, which is a set defined as the intersection of finitely many half spaces, each of which is defined by a linear inequality. Its objective function is a real-valued affine (linear) function defined on this polyhedron.</p> <br> <div style='text-align: center; clear:both;'><a id='solvertool' href='javascript:loadsolver();' style='display:none' class='btn-ok'>No tool solver</a></div>";
    document.getElementById("solvertool").innerHTML = "Linprog Solver";
    document.getElementById("solvertool").style = "visibility: true";
    sessionStorage.setItem("button", 4);
}
function queuing(){
    document.getElementById("main_content").innerHTML = '<h1 style="text-align: left">Queuing theory</h1><p>Queueing theory is the mathematical study of waiting lines, or queues. A queueing model is constructed so that queue lengths and waiting time can be predicted. Queueing theory is generally considered a branch of operations research because the results are often used when making business decisions about the resources needed to provide a service. Queueing theory has its origins in research by Agner Krarup Erlang when he created models to describe the system of Copenhagen Telephone Exchange company, a Danish company. The ideas have since seen applications including telecommunication, traffic engineering, computing and, particularly in industrial engineering, in the design of factories, shops, offices and hospitals, as well as in project management.</p><br> <div style=\'text-align: center; clear:both;\'><a id=\'solvertool\' href=\'javascript:loadsolver();\' style=\'display:none\' class=\'btn-ok\'>No tool solver</a></div>';
    document.getElementById("solvertool").innerHTML = "Queuing Solver";
    document.getElementById("solvertool").style = "visibility: true";
    sessionStorage.setItem("button", 2);
    /*document.getElementById("model1").innerHTML = "M/M/1:∞,FIFO system";
    document.getElementById("model2").innerHTML = "M/M/S:∞,FIFO system";
    document.getElementById("model3").innerHTML = "M/M/1:LQ,FIFO system";
    document.getElementById("model4").innerHTML = "M/M/1:LQ,FIFO (rho=1)";
    document.getElementById("model5").innerHTML = "M/M/S:LQ,FIFO system";
    document.getElementById("model6").innerHTML = "M/M/1:LS,FIFO system";
    document.getElementById("model7").innerHTML = "M/M/S:LS,FIFO system";
    document.getElementById("model1").style = "display: true";
    document.getElementById("model2").style = "display: true";
    document.getElementById("model3").style = "display: true";
    document.getElementById("model4").style = "display: true";
    document.getElementById("model5").style = "display: true";
    document.getElementById("model6").style = "display: true";
    document.getElementById("model7").style = "display: true";*/
}
function inventory() {
    document.getElementById("main_content").innerHTML  = "<h1 style='text-align: left'>Inventory</h1> <p> Inventory refers to the goods and materials that a business holds for the ultimate goal of resale, production or utilisation. Inventory management is a discipline primarily about specifying the shape and placement of stocked goods. It is required at different locations within a facility or within many locations of a supply network to precede the regular and planned course of production and stock of materials. The concept of inventory, stock or work in process (or work in progress) has been extended from manufacturing systems to service businesses and projects. In the context of a manufacturing production system, inventory refers to all work that has occurred – raw materials, partially finished products, finished products prior to sale and departure from the manufacturing system. </p><br> <div style='text-align: center; clear:both;'><a id='solvertool' href='javascript:loadsolver();' style='display:none' class='btn-ok'>No tool solver</a></div>";
    document.getElementById("solvertool").innerHTML = "Inventory Solver";
    document.getElementById("solvertool").style = "visibility: true";
    /*document.getElementById("model1").innerHTML = "General model";
    document.getElementById("model2").innerHTML = "EPQ model";
    document.getElementById("model3").innerHTML = "EOQ model";
    document.getElementById("model4").innerHTML = "EOQ with shortage";
    document.getElementById("model5").style = "display: none";
    document.getElementById("model6").style = "display: none";
    document.getElementById("model7").style = "display: none";*/
    sessionStorage.setItem("button", 1);
}
function about(){
    document.getElementById("solvertool").style = "display: none";
    document.getElementById("main_content").innerHTML  = "<br> <p style='border-style:none; text-indent:0px'>Andrey Vinajera Zamora <br> Industrial Engineer (2007)<br> Master degree in technical sciences (2011) <br> PhD degree in technical science (2017) <br> Group of Maths-applied  <br> Field of interest: Python data science, Operation research, Statistics.</p>"
    sessionStorage.setItem("button", 5);
}
function contact(){
    document.getElementById("main_content").innerHTML  = "<br> <p style='border-style:none; text-indent:0px'>Andrey Vinajera Zamora <br> avinajera2011@gmail.com <br> Faculty of Mechanics and Industrial engineering<br> Central University 'Marta Abreu' de Las Villas <br> Santa Clara, Villa Clara. Cuba</p>";
    document.getElementById("solvertool").style = "display: none";
    sessionStorage.setItem("button", 6);
}
function update_description(page) {
    var b = sessionStorage.getItem('button');
    if (b==null) {
        console.log('HOME')
        home();
    } else {
        if (page == "inventory")  {
            if (b == 1) {
                inventory_home();
            } else if (b == 3) {
                inventory_measures();
            } else {
                inventory_legend();
            }
        } else if (page == "home") {
            if (b == 2) {
                queuing();
            } else if (b == 3) {
                inventory();
            } else if (b==4) {
                linprog();
            } else if (b==5) {
                about();
            }
            else if (b==6) {
                contact();
            } else {
                home();
            }
        }
    }
}
function loadsolver() {
    if  (document.getElementById("solvertool").innerHTML == "Inventory Solver") {
        window.location.href = "inventory/";
    } else if  (document.getElementById("solvertool").innerHTML == "Linprog Solver") {
        window.location.href = "linprog/";
        //window.location.href = "linprog.html";
    } else if  (document.getElementById("solvertool").innerHTML == "Queuing Solver") {
        window.location.href = "queuing/";
    } else  {
        alert("Please, select any academic field");
    } 
}
/*  #################################  INVENTORY PAGES  ##############################################*/
function get_inv_solution() {
    document.getElementById("system").innerHTML = sessionStorage.getItem('system');
//    document.getElementById("Q").innerHTML = Number(JSON.parse(sessionStorage.getItem('Q'))).toFixed(0);
//    document.getElementById("S").innerHTML = Number(JSON.parse(sessionStorage.getItem('S'))).toFixed(0);
//    document.getElementById("t1").innerHTML = Number(JSON.parse(sessionStorage.getItem('t1'))).toFixed(4);
//    document.getElementById("t2").innerHTML = Number(JSON.parse(sessionStorage.getItem('t2'))).toFixed(4);
//    document.getElementById("t3").innerHTML = Number(JSON.parse(sessionStorage.getItem('t3'))).toFixed(4);
//    document.getElementById("t4").innerHTML = Number(JSON.parse(sessionStorage.getItem('t4'))).toFixed(4);
//    document.getElementById("T").innerHTML = Number(JSON.parse(sessionStorage.getItem('T'))).toFixed(4);
//    document.getElementById("f").innerHTML = Number(JSON.parse(sessionStorage.getItem('f'))).toFixed(4);
//    document.getElementById("B").innerHTML = Number(JSON.parse(sessionStorage.getItem('B'))).toFixed(0);
//    document.getElementById("IC").innerHTML = Number(JSON.parse(sessionStorage.getItem('IC'))).toFixed(2);
//    document.getElementById("PC").innerHTML = Number(JSON.parse(sessionStorage.getItem('PC'))).toFixed(2);
//    document.getElementById("TC").innerHTML = Number(JSON.parse(sessionStorage.getItem('TC'))).toFixed(2);
//    document.getElementById("q_lbl").innerText =   sessionStorage.getItem('unit');
//    document.getElementById("s_lbl").innerText =   sessionStorage.getItem('unit');
//    document.getElementById("t1_lbl").innerText =   sessionStorage.getItem('time_unit');
//    document.getElementById("t2_lbl").innerText =   sessionStorage.getItem('time_unit');
//    document.getElementById("t3_lbl").innerText =   sessionStorage.getItem('time_unit');
//    document.getElementById("t4_lbl").innerText =   sessionStorage.getItem('time_unit');
//    document.getElementById("T_lbl").innerText =   sessionStorage.getItem('time_unit');
//    document.getElementById("B_lbl").innerText =   sessionStorage.getItem('unit');
//    document.getElementById("f_lbl").innerText =   "t/" + sessionStorage.getItem('time_unit');
//    document.getElementById("pc_lbl").innerText =   "$";
//    document.getElementById("ic_lbl").innerText =   "$";
//    document.getElementById("tc_lbl").innerText =   "$";
}
function update_units() {
    document.getElementById("demand_lbl").innerText = "(" + String(document.getElementById("unit").value) + " per " + document.getElementById("time_unit").value + ")"
    document.getElementById("production_rate_lbl").innerText = "(" + String(document.getElementById("unit").value) + " per " + document.getElementById("time_unit").value + ")"
}
//function solve_model() {
//    var D = Number(document.getElementById("demand").value);
//    var c = Number(document.getElementById("unit_cost").value);
//    sessionStorage.setItem("time_unit", document.getElementById("demand").value)
//    var h = Number(document.getElementById("holding_cost").value);
//    var A = Number(document.getElementById("launch_cost").value);
//    var psi = Number(document.getElementById("production_rate").value);
//    var pi = Number(document.getElementById("shortage_cost").value);
//    if (document.getElementById("select_model").value == "General") {
//        sessionStorage.setItem("system", "General");
//        var uno = 2 * D * A / h;
//        var dos = 1 / (1 - D / psi);
//        var tres = h / pi + 1;
//        var Q = Math.pow(uno * dos * tres, 0.5);
//        var t2 = Math.pow(2 * pi * A * (1 - D / psi) / (D * h * (h + pi)), 1/2);
//        var S = D * t2;
//        var t1= S / (psi - D);
//        var t3 = Math.sqrt(2 * h * A * (1 - D / psi) / (D * pi * (h + pi)));
//        var B = D * t3;
//        var t4 = B / (psi - D);
//        var IC = h * S * (t1 + t2) / 2;
//        var DC = pi * B + (t3 + t4);
//        var PC = c * Q + A;
//        var TC = IC + DC + PC;
//    } else if (document.getElementById("select_model").value == "Economic Production Quantity (EPQ)") {
//        sessionStorage.setItem("system", "EPQ");
//        var Q = Math.sqrt(2 * D * A  * (1 / (1 - D / psi)) / h);
//        var t2 = Math.sqrt(2 * A * (1 - D / psi) / (D * h));
//        var t1 = t2 * D / (psi - D);
//        var t3 = 0;
//        var t4 = 0;
//        var S = D * t2;
//        var IC = h * S * (t1 + t2) / 2;
//        var B = 0;
//        var PC = c * Q + A;
//        var TC = IC + PC;
//    }  else if (document.getElementById("select_model").value == "Economic Order Quantity (EOQ)") {
//        sessionStorage.setItem("system", "EOQ");
//        var Q = Math.sqrt(2 * D * A / h);
//        var S = Q;
//        var t1 = Q / D;
//        var t2 = 0;
//        var t3 = 0;
//        var t4 = 0;
//        var B = 0;
//        var IC = h * S * t1 / 2;
//        var PC = A;
//        var TC = IC + PC;
//    } else {
//        sessionStorage.setItem("system", document.getElementById("select_model").value);
//        var Q = Math.sqrt(2 * D * A * (h + pi) / (h * pi));
//        var B = Math.sqrt(2 * D * h * A / ((h + pi) * pi));
//        var S = Q - B;
//        var t1 = Math.sqrt(2 * pi * A / (D * pi * (h + pi)));
//        var t2 = D / D;
//        var t3 = 0;
//        var t4 = 0;
//        var IC = h * S * t1 / 2;
//        var PC = A;
//        var DC = pi * B * t2 / 2;
//        var TC = IC + PC + DC;
//    }
//    var T = Q / D;
//    var f = D / Q;
//    sessionStorage.setItem("Q", Q);
//    sessionStorage.setItem("t1", t1);
//    sessionStorage.setItem("t2", t2);
//    sessionStorage.setItem("t3", t3);
//    sessionStorage.setItem("t4", t4);
//    sessionStorage.setItem("T", T);
//    sessionStorage.setItem("f", f);
//    sessionStorage.setItem("S", S);
//    sessionStorage.setItem("IC", IC);
//    sessionStorage.setItem("PC", PC);
//    sessionStorage.setItem("TC", TC);
//    sessionStorage.setItem("B", B);
//    sessionStorage.setItem("S", S);
//    //console.log("result " + Array(Q, t1, t2, t3, t4, T, f, S, IC, PC, TC, B, S))
//    sessionStorage.setItem("unit", document.getElementById("unit").value );
//    sessionStorage.setItem("time_unit", document.getElementById("time_unit").value );
//}
function check_data() {
    //solve_model();
    window.location.href = "results/";
    // Button to load on page
}
function get_data_saved(){
    document.getElementById('demand').innerText = sessionStorage.getItem('demand');
}
function inventory_home() {
    document.getElementsByClassName("description_zone")[0].innerHTML = "<h1 style='text-align: center;'> Main features in the models:</h1> <ul><li><u>General</u>: initial inventory is zero, production rate, shortage, four time's intervals.</li><i>Data required</i>:all of them. <li><u>Economic Production Quantity (EPQ)</u>: initial inventory is zero, production rate, no shortage, two time's intervals.</li><i>Data required</i>: all except unit shortage cost.<li><u>Economic Order Quantity (EOQ)</u>: no shortage, instant replenishment, one time's intervals</li><i>Data required</i>: all, except unit shortage cost and production rate<li><u>EOQ with shortage</u>: initial inventory is greater than zero, shortage, one time's intervals</li><i>Data required</i>:all except production rate</ul>";
}
function inventory_legend() {
    document.getElementsByClassName("description_zone")[0].innerHTML = "<h1 style='text-align: center;'> Legend:</h1> <ul> <li>r: constant production rate</li> <li>a: constant demand</li> <li>c: production's unit cost</li> <li>h: unit holding cost</li> <li>u: unit shortage cost</li> <li>k: order or setup cost per order</li></ul>";
    sessionStorage.setItem("button", 2);
}
function inventory_measures() {
    document.getElementsByClassName("description_zone")[0].innerHTML = "<h1 style='text-align: center';> Performance measures:</h1> <ul><li>Q: Quantity to order (buy or production)</li><li>T: period (time between to orders) </li><li>f: frequency (number of orders by unit of time) </li><li>S: maximum level of inventory</li><li>d: maximun quantity of umits in shortage</li><li>t<sub>1</sub><sup>*</sup>, t<sub>2</sub><sup>*</sup>, t<sub>3</sub><sup>*</sup>, t<sub>4</sub><sup>*</sup>: Intervals of time</li><li>C(P): production cost</li><li>C(D): shortage cost</li><li>C(I): inventory cost</li><li>C(T): total cost</li></ul> <br><br> ";
    sessionStorage.setItem("button", 3);
}
