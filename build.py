import glob

def build():
    with open('src/template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    slides_content = []
    
    slide_files = sorted(glob.glob('src/slides/*.html'), key=lambda x: int(x.split('/')[-1].split('.')[0]))
    
    for i, slide_file in enumerate(slide_files):
        with open(slide_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        # Add the wrapper cleanly
        active_class = " active" if i == 0 else ""
        wrapper_start = f'    <!-- Slide {i+1} -->\n    <div class="slide{active_class}" id="slide-{i+1}">\n'
        wrapper_end = f'\n    </div>\n'
        
        # Indent content correctly for neatness
        indented_content = "\n".join("      " + line for line in content.split("\n"))
        
        slides_content.append(wrapper_start + indented_content + wrapper_end)
        
    final_content = template.replace('    <!-- SLIDES_GO_HERE -->\n', "".join(slides_content))
    
    with open('slides.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Build successful: Merged {len(slides_content)} slides into slides.html")

if __name__ == "__main__":
    build()
