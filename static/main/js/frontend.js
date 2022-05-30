$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        rtl: true,
        loop: false,
        margin: 10,
        nav: true,
        stagePadding: 25,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })

    $('.counter').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });


    //block of code to progress navbar
    // window.onscroll = function () {
    //     myFunction()
    // };

    // function myFunction() {
    //     var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    //     var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    //     var scrolled = (winScroll / height) * 100;
    //     document.getElementById("myBar").style.width = scrolled + "%";
    // }
    //block of code to progress navbar



//     $(function () {
//         $(".navbar").attr("id", "navbar");
//         //remove background on top and animated
//         $(document).scroll(function () {
//             if ($(window).scrollTop() === 0) {
//                 $(".navbar").removeClass("bg-dark  shadow-3");
//                 $(".progress-container").css("opacity", "0");
//                 $("#navbar").css("top", "2rem");
//             } else {
//                 $(".navbar").addClass("bg-primary shadow-3");
//                 $(".progress-container").css("opacity", "1");
//                 $("#navbar").css("top", "0rem");
//             }
            
//         });
//         //bootstrap event collapse
//         $("#navbarNavAltMarkup").on("show.bs.collapse", function () {
//             $("#navbarNavAltMarkup").addClass("bg-primary rounded-3 p-3 mt-4");
//         });
//     });




  });