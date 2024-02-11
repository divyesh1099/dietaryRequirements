

    document.addEventListener('DOMContentLoaded', function() {
        var controller = new ScrollMagic.Controller();

        new ScrollMagic.Scene({
            triggerElement: "#greeting",
            triggerHook: 0,
            duration: "100%" // bind scroll to the height of the window
        })
        .setTween("#greeting", {opacity: 0}) // fade out greeting
        .addTo(controller);

        gsap.to("#greeting", {duration: 2, opacity: 1, ease: "power2.inOut"}); // Initial fade in for greeting

        // Questions fade in and out
        gsap.utils.toArray('.section').forEach(function(section, index) {
            if(index !== 0) { // Skip greeting section
                new ScrollMagic.Scene({
                    triggerElement: section,
                    triggerHook: 0.5,
                    duration: "100%" // Make sure the fade out completes before the section scrolls out of view
                })
                .setTween(section, {opacity: 1, duration: 1}) // fades in
                .addTo(controller);

                // Add a new ScrollMagic scene for fading out
                new ScrollMagic.Scene({
                    triggerElement: section,
                    triggerHook: 0, // Start at the top of the section
                    duration: "100%" // Duration covers the whole section
                })
                .setTween(section, {opacity: 0, duration: 1}) // fades out
                .addTo(controller);
            }
        });
    });