gsap.registerPlugin(ScrollTrigger);

  const flightPath = {
    curviness: 1.25,
    autoRotate: true,
    path: [
      { x: 100, y: -20 },
      { x: 300, y: 10 },
      { x: 500, y: 100 },
      { x: 750, y: -100 },
      { x: 350, y: -50 },
      { x: 600, y: 100 },
      { x: 800, y: 0 },
      { x: window.innerWidth, y: -250 },
    ]
  };

  const tween = gsap.timeline({
    scrollTrigger: {
      trigger: ".animation",
      start: "top center", // when the top of the trigger hits the center of the viewport
      end: "bottom top", // when the bottom of the trigger hits the top of the viewport
      scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
    }
  });

  tween.to(".paper-plane", {
    motionPath: flightPath,
    ease: "none" // linear animation for smooth scrubbing
  });