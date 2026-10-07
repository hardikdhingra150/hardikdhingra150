"""GitHub-native shared race. Only exact move titles are accepted."""
import argparse, json, random, re, subprocess
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / 'game/state.json'
LANES = ['left', 'centre', 'right']
REPO = 'hardikdhingra150/hardikdhingra150'
PATTERN = re.compile(r'^HD150\|(\d+)\|(left|centre|right|restart)$')

def save(state):
    STATE.write_text(json.dumps(state, indent=2) + '\n')

def render(state):
    blocked = state['blocked']
    s = '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="480" viewBox="0 0 1280 480" role="img" aria-label="Shared racing board. Choose a clear lane using the links below.">'
    s += '<rect width="1280" height="480" rx="12" fill="#10151c"/>'
    def text(x,y,value,size=18,color='#efeee7'):
        return f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" fill="{color}">{escape(str(value))}</text>'
    s += text(30,37,'05 / GITHUB GRID RUN',13,'#f23b2c')
    s += text(30,87,'SHARED RACE / EVERY VISITOR CAN TAKE A TURN',21)
    s += text(30,124,f"CLEARED {state['score']}  /  BEST {state['best']}  /  TURN {state['turn']}",14,'#a4afb8')
    for i,lane in enumerate(LANES):
        x=290+i*310
        s += f'<rect x="{x}" y="165" width="240" height="260" rx="7" fill="#202b36"/>'
        s += text(x+27,200,lane.upper(),18)
        if lane in blocked:
            s += f'<path d="M{x+90} 226L{x+61} 287H{x+119}Z" fill="#f23b2c"/>'
            s += text(x+85,274,'!',27)
            s += text(x+25,320,'BLOCKED',18,'#ff6a58')
        else:
            s += text(x+28,272,'↓',47,'#8be7a4')
            s += text(x+25,320,'CLEAR',18,'#8be7a4')
        if state['lane']==lane:
            s += f'<rect x="{x+98}" y="351" width="30" height="53" rx="6" fill="#f23b2c"/><path d="M{x+84} 355H{x+142}M{x+84} 397H{x+142}" stroke="#f23b2c" stroke-width="7"/>'
    s += text(30,460,'SESSION ENDED — RESTART BELOW' if state['over'] else 'SPOT THE CLEAR LANE. SUBMIT A MOVE BELOW.',13,'#f23b2c')+'</svg>'
    (ROOT/'assets/race-board.svg').write_text(s)
    def link(lane,label):
        title=f"HD150%7C{state['turn']}%7C{lane}"
        return f'[{label}](https://github.com/{REPO}/issues/new?title={title}&body=GitHub%20Grid%20Run%20move.%20Submit%20this%20issue%20to%20play.)'
    controls = link('restart','↻ START A NEW RUN') if state['over'] else ' &nbsp; / &nbsp; '.join(link(x,'◀ LEFT' if x=='left' else '◆ CENTRE' if x=='centre' else 'RIGHT ▶') for x in LANES)
    readme=ROOT/'README.md'; content=readme.read_text()
    content=re.sub(r'<!-- RACE-CONTROLS:START -->.*?<!-- RACE-CONTROLS:END -->','<!-- RACE-CONTROLS:START -->\n\n'+controls+'\n\n<!-- RACE-CONTROLS:END -->',content,flags=re.S)
    readme.write_text(content)

def gh(*args):
    return subprocess.check_output(['gh',*args],text=True)

def process():
    state=json.loads(STATE.read_text())
    # Drain all open matching moves, including runs superseded by concurrency.
    pages=json.loads(gh('api',f'repos/{REPO}/issues?state=open&sort=created&direction=asc&per_page=100','--paginate','--slurp'))
    issues=[issue for page in pages for issue in page]
    for issue in issues:
        if 'pull_request' in issue: continue
        match=PATTERN.fullmatch(issue['title'])
        if not match: continue
        turn,choice=match.groups(); number=str(issue['number'])
        if int(turn)!=state['turn']:
            message='That turn has already changed. Refresh the profile README and choose from the current board.'
        elif choice=='restart' and state['over']:
            state.update(score=0,over=False,lane='centre',blocked=random.sample(LANES,2),turn=state['turn']+1)
            message='New race started. Choose the clear lane on the current board.'
        elif state['over'] or choice=='restart':
            message='This move is unavailable for the current session. Refresh the profile README.'
        else:
            state['lane']=choice;state['turn']+=1
            if choice in state['blocked']:
                state['over']=True
                message=f"Traffic caught you. The shared race finished with {state['score']} clear turns. Restart from the README."
            else:
                state['score']+=1;state['best']=max(state['best'],state['score']);state['blocked']=random.sample(LANES,2)
                message=f"Clean move! Shared score: {state['score']}. Refresh the README for the next board."
        save(state);render(state)
        gh('issue','comment',number,'--repo',REPO,'--body',message)
        gh('issue','close',number,'--repo',REPO,'--reason','completed')

if __name__=='__main__':
    args=argparse.ArgumentParser();args.add_argument('--process',action='store_true');opt=args.parse_args()
    if opt.process:process()
    else:render(json.loads(STATE.read_text()))
