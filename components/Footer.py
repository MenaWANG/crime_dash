from dash import html
from utils.consts import LINKEDIN_PROFILE



Footer = html.Div(html.H6(["©2023, Developed and Maintained By ", 
                           html.A("Mena Ning Wang" , 
                                  href=LINKEDIN_PROFILE, 
                                  target="_blank",
                                  style={"color": "LightSeaGreen"})]), 
                  className="mt-9")