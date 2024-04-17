from collections import defaultdict
from collections import OrderedDict

def main() :
    text =  "A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit! What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid."
    text = text.lower().split()
    d = defaultdict(lambda: 0)
    for word in text :
        d[word] += 1
        
    od = OrderedDict(sorted(d.items(), key = lambda x : x[1], reverse = True))
    print(od)
    
if __name__ == "__main__" :
    main()