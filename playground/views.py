from django.shortcuts import render

lang_urls = {
    'cpp': 'https://www.jdoodle.com/embed/v0/4SSy',
    'c': 'https://www.jdoodle.com/embed/v0/4STr',
    'cs': 'https://www.jdoodle.com/embed/v0/4STt',
    'dart': 'https://www.jdoodle.com/embed/v0/4STx',
    'go': 'https://www.jdoodle.com/embed/v0/4STy',
    'java': 'https://www.jdoodle.com/embed/v0/4STz',
    'nodejs': 'https://www.jdoodle.com/embed/v0/4STA',
    'php': 'https://www.jdoodle.com/embed/v0/4STB',
    'py': 'https://www.jdoodle.com/embed/v0/4STD',
    'rust': 'https://www.jdoodle.com/embed/v0/4STH',
    'ruby': 'https://www.jdoodle.com/embed/v0/4STJ',
    'asm': 'https://www.jdoodle.com/embed/v0/4STL',
    'prolog': 'https://www.jdoodle.com/embed/v0/4STN',
    'bash': 'https://www.jdoodle.com/embed/v0/4STO',
    'sql': 'https://www.jdoodle.com/embed/v0/4STP',
    'r': 'https://www.jdoodle.com/embed/v0/4STS'
    
}


# Create your views here.
def playground(request):
    try:
        lang_url = lang_urls[request.GET["lang"]]
        
    except:
        lang_url = None
        
    return render(request,"playground.html", {'lang_url': lang_url, 'title': 'الملعب'})
