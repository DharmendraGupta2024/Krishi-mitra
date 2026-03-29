import os
import re

details_files = [
    'seed/fertilizer/detail.html',
    'seed/fertilizer/detail2.html',
    'seed/fertilizer/detail3.html',
    'seed/fertilizer/detail4.html'
]

modern_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    
    <!-- Base resets and styles to match Feedback page -->
    <link rel="stylesheet" href="../../plugins/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../plugins/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/responsive.css">
    
    <!-- Premium UI -->
    <link rel="stylesheet" href="../../css/premium.css">
</head>
<body>

<!-- Start mainmenu -->
<header>
    <div class="header">
        <a href="../../index.html" class="logo"><img src="../../images/footer-logo.png" alt="logo"></a>
        <div class="header-right">
            <div class="subnav">
                <button class="subnavbtn">Weather<i class="#"></i></button>
                <div class="subnav-content">
                    <li><a href="../../weatherwebsite/index.html">Search</a></li>
                    <li><a href="../../weatherwebsite/currentLocationW/index.html">Your Current Location</a></li>
                </div>
            </div>
            <a href="../../govts.html" class="subnavbtn">Government Schemes</a>
            <div class="subnav">
                <button class="subnavbtn">Crop<i class="#"></i></button>
                <div class="subnav-content">
                    <li><a href="../../seed.html">Info on Seeds</a></li>
                    <li><a href="../../seed price.html">Current Seeds Price</a></li>
                    <li><a href="../../Fertilizer.html">Fertilizer</a></li>
                </div>
            </div>
            <div class="subnav">
                <button class="subnavbtn">Tech Knowledge<i class="#"></i></button>
                <div class="subnav-content">
                    <li><a href="../../solarpanel.html">Solar Panel</a></li>
                    <li><a href="../../tech.html">Modern Day Tech</a></li>
                </div>
            </div>
            <a href="../../Feedback.html" class="subnavbtn">Feedback</a>
        </div>
    </div>
</header>
<!-- End mainmenu -->

<section class="subpage-hero">
    <h1>{article_title}</h1>
</section>

<section class="modern-section" style="padding-top: 50px;">
    <div class="thm-container">
        <div class="split-showcase" style="align-items: flex-start;">
            <div class="split-showcase-img" style="flex: 1;">
                <img src="{img_src}" alt="Fertilizer Image" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); width: 100%;">
            </div>
            <div class="split-showcase-text" style="flex: 2; padding-left: 40px; font-size: 16px; line-height: 1.8; color: var(--text-dark);">
                {content_body}
            </div>
        </div>
    </div>
</section>

<section class="bottom-bar" style="margin-top: 60px;">
    <div class="thm-container clearfix">
        <div class="pull-left">
            <p>dharmendra gupta All rights reserved.</p>
        </div>
        <div class="pull-right">
            <a href="#">Created By : <i>dharmendra gupta</i> </a>
        </div>
    </div>
</section>

<!-- Back to Top Button -->
<a href="#" class="back-to-top" id="backToTopBtn" aria-label="Go to top">↑</a>
<script src="../../js/custom.js"></script>

</body>
</html>
"""

for f in details_files:
    if not os.path.exists(f):
        print(f"File {f} not found!")
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
        
    # Extract Title from <title> or <h3>
    title_match = re.search(r'<title>(.*?)</title>', html)
    page_title = title_match.group(1).strip() if title_match else "Fertilizer Detail"
    
    article_title_match = re.search(r'<h3><a href="#">(.*?)</a></h3>', html)
    article_title = article_title_match.group(1).strip() if article_title_match else page_title
    
    # Extract Image
    img_match = re.search(r'<img src="(img/.*?)"', html)
    img_src = img_match.group(1).strip() if img_match else ""
    
    # Extract Content
    # the content usually starts after the <h3> and ends before </div>
    # we'll grab everything between </h3> and </div> for class="blog_1r"
    blog_match = re.search(r'<div class="blog_1r">.*?</h3>(.*?)</div>', html, flags=re.DOTALL)
    if blog_match:
        content_body = blog_match.group(1).strip()
    else:
        # Fallback
        content_body = "<p>Information coming soon.</p>"
        
    # Replace content_body <p> tags with inline styles for better formatting or leave them to premium.css
    # premium.css has basic p formatting but we'll leave it as is.
    
    new_html = modern_template.format(
        page_title=page_title,
        article_title=article_title,
        img_src=img_src,
        content_body=content_body
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_html)
    print(f"Upgraded UI for {f}")

print("Done upgrading detail files!")
