// 渠道页演示数据（假的，地址都是 .example）
export const M=['gpt-5.1:128K','gpt-5.1-mini:128K','claude-sonnet-4.5:200K','claude-haiku-4.5:200K','gemini-2.5-pro:1M','deepseek-v3.2:128K','qwen3-max:256K','gpt-4o:128K','o3:200K','claude-opus-4.1:200K','gemini-2.5-flash:1M','kimi-k2:256K','glm-4.6:200K'];
export const CH=[
 {n:'主渠道',h:'api.mint.example',f:'OpenAI',r:2,now:1,k:[['3f9a','','正常'],['c21e','','正常'],['77b0','cool','冷却 4 分']],m:[0,1,2,4,7,8,9,3,10,5,11,12,6]},
 {n:'备用渠道',h:'relay.cocoa.example',f:'Anthropic',r:1,k:[['a8d2','bad','超时']],m:[3,2]},
 {n:'奶盖中转',h:'foam.relay.example',f:'OpenAI',r:2,k:[['0e1c','cool','冷却 12 分'],['5b9d','','正常']],m:[0,5]},
 {n:'薄荷站',h:'mint2.example',f:'OpenAI',r:3,k:[['91aa','','正常']],m:[0,1]},
 {n:'可可站',h:'cocoa.example',f:'Anthropic',r:2,k:[['d4f0','','正常'],['2a7e','','正常']],m:[2,3]},
 {n:'焦糖站',h:'caramel.example',f:'OpenAI',r:1,k:[['6c3b','','正常']],m:[6]},
 {n:'柚子站',h:'yuzu.example',f:'OpenAI',r:2,k:[['e801','','正常']],m:[5,6]},
 {n:'海盐站',h:'seasalt.example',f:'Gemini',r:2,k:[['47ad','','正常']],m:[4]},
 {n:'布丁站',h:'pudding.example',f:'OpenAI',r:1,k:[['b3e9','','正常'],['f05c','','正常']],m:[0]},
 {n:'云朵站',h:'cloud.example',f:'OpenAI',r:2,k:[['8d21','','正常']],m:[1,5]},
 {n:'晚风站',h:'breeze.example',f:'Anthropic',r:2,k:[['c7a4','','正常']],m:[3]},
 {n:'抹茶站',h:'matcha.example',f:'OpenAI',r:1,k:[['1f6e','','正常']],m:[6]},
 {n:'月亮站',h:'moon.example',f:'OpenAI',r:2,k:[['29bd','','正常']],m:[0,6]},
 {n:'旧站',h:'old.example',f:'OpenAI',r:1,off:1,k:[['00a3','off','停用']],m:[0]}
];
CH.forEach(c=>c.m=c.m.map(j=>{const[a,b]=M[j].split(':');return{n:a,w:b,o:/1M/.test(b)?'64K':/claude|o3/.test(a)?'32K':'16K',v:/gpt-5|claude|gemini|4o|o3|qwen3/.test(a)?1:0,s:/o3/.test(a)?0:1}}));
export const UP=['gpt-5.1','gpt-5.1-mini','gpt-5.1-nano','gpt-4o','gpt-4o-mini','o3','o4-mini','claude-opus-4.1','claude-sonnet-4.5','claude-haiku-4.5','gemini-2.5-pro','gemini-2.5-flash','gemini-2.5-flash-lite','deepseek-v3.2','deepseek-r1','qwen3-max','qwen3-coder','kimi-k2','glm-4.6','grok-4'];
export const WO=['32K','128K','200K','256K','1M'],OO=['4K','8K','16K','32K','64K'];
export const worst=c=>c.off?'off':c.k.some(x=>x[1]=='bad')?'bad':c.k.some(x=>x[1]=='cool')?'cool':'';
export const EP={OpenAI:'/v1/chat/completions',Anthropic:'/v1/messages',Gemini:'/v1beta/models/{模型}:generateContent'}
export const FM=['OpenAI','Anthropic','Gemini'],RT=[1,2,3,4,5]
