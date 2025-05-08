// HomePage.jsx
import React from "react";
import Slider from "react-slick";
import { Box, Typography, Card, CardMedia, CardContent } from "@mui/material";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

const cards = [
  {
    title: "Explore Phuket",
    description: "Beautiful beaches and vibrant nightlife.",
    image: "https://source.unsplash.com/600x400/?phuket",
  },
  {
    title: "Discover Krabi",
    description: "Scenic views and peaceful resorts.",
    image: "https://source.unsplash.com/600x400/?krabi",
  },
  {
    title: "Island Hopping",
    description: "Visit multiple islands in one trip.",
    image: "https://source.unsplash.com/600x400/?island",
  },
];

const sliderSettings = {
  dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 3000,
};

const HomePage = () => {
  return (
    <Box sx={{ padding: 4 }}>
      <Typography variant="h3" align="center" gutterBottom>
        Plan Your Dream Trip
      </Typography>

      <Box sx={{ maxWidth: 600, margin: "0 auto" }}>
        <Slider {...sliderSettings}>
          {cards.map((card, index) => (
            <Card key={index} sx={{ margin: 2 }}>
              <CardMedia component="img" height="300" image={card.image} alt={card.title} />
              <CardContent>
                <Typography variant="h5">{card.title}</Typography>
                <Typography variant="body2" color="text.secondary">
                  {card.description}
                </Typography>
              </CardContent>
            </Card>
          ))}
        </Slider>
      </Box>
    </Box>
  );
};

export default HomePage;
