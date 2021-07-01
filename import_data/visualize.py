import cv2
import numpy as np

MARKET = """
##################
##..............##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()


class Visualize_Simulation:
    """
    Class of tools for visualizing the simulation.
    """


MARKET_COLOR = """
   . 8t%;%;t;S. ;S:  8    .   .   .     .        .  . . .  . . . 8;StX%StS. tXt;:8..  .           . :.%S;tXS:   . t% 
 .   . . @X8S8@8X8X8X8@88SXSS8t8@88S%88888 .  .  :tt;t;t;t;t;;t;t;t;;;t;%;t;;t;S;t;t;t;ttttt:.:    . %.%S%@ .  .;:t%
    .  .:8  % S S X X S X%SXXtS X XXXt%  :@..  . @@;tt%88SS%SS%SSSSSSSSSXSSSS%SSSXt%SS%;tt%%%.8;.   .      ...:;8X %
 .    . @t ;                 .     . . .8  :.    @ttXX8X% .  . X@XXXX8X88X%  .   .t . X.@XX. .8;  .   .;8SXSSSSS8@.t     
   . . %% @ .    ; :  8:S%X.. 8;8 .   . 8  X.. . @8@@SX8%  . . 8:t%S%Sttt.8 .  . .8  ;888X8. .@:    .  :t.8X%%%%Xt;%
 .   . %.8:.    .%%.     :; ..:;:   .  ..:88.. . 88SSXSX% .   .8;;88%t%%t%; .   ..S888@@@@@88@%S.. . . ;S:.:XSSSXS%%
    . :X8@   .....:....:..:......:..  . .: ;:  . .;;:;:%:. .. .   ..   .   . .. . ;;;;;;;;;;;;t:   :;;.t8:;;;t;;t;;%
  .  .:t.. . S  :..:.:..::.:::::.:.8   . X.;%%8;8tSXSXX@@XXXXXXX@XX@X@XXXXXXXXXXXXXXXXXXXXXXXS88 . @@8;:ttttt;tt;;;%
   . @XS .   X    .. . .           .          %;X:S.%                   8%.t                   : . S88:%%:@8@8SS..t%
.  . . .     @88@SS8t%%S%%%t%%%%%%SS         X888X88@X                 .S@88                     . %88.t88@8X;@t:.t%
  . XSS . .  .%;..:%X8X8S @X;.. . .            .                           .                     . S88.....88t%%%%:%
  . .  .    :@;. t888.    %888.  . S888:    t8@8.    :888t      8X@:     @88X      %@X%     @88;.  t88.. . ;t%:;;@t%
 . tS8:t .  @;S. 8%:;X... 8;:;S .  Xtt;;    @t;;%. . %tt%X     @%;%X     .tt:      .S8@:     %8... X88:;..:@SS@@Xtt%
 . @t @: .  %8:..8t:;S  . 8:;:S .. @;:.;  . 8t::% . .t:;;8     @;::@    .:;;t      :SX@ :   tX  .. t88%t:;t%t%t%%t:%
 . 8t 8; .. %XX..8;::X .  8:;:S  . @t:.t .. 8;:.%  . %::t@ .   8;:;X .   :;;t     .:t8@ ..       . S88.. . . .  ..%%
 . @t S: .  ;S.. 8t::S .. 8:;:S .  X;;.;  . 8t::t. . t:;;@ . . @;:;X   . :;;; .t; .;;8@ .S:   . ;t %@8..       .  t%
 . 8;.    . X;S .8;:;X  . 8:;:S %8 X;:.t SX @;::% 8S %::t@  %@ 8;::@ .  .:;;t  S. .:;8:  :8.%8@ 8  t88..  . .   . t%
 . @;.  .   .. . 8t::S .  8:;:S .X X;;.t :% @;::% % .%:;;@   X 8;:;X .  .:;;t. %t..:%88  tX  88:t; X88..     .  . t%
 . 8%:8X .     . 8%;tX .. 8t::S .X X;:.;..t @;::% %. %::;@  .S 8;:;X .   :;;t  X8 .:;88  .8: 8@ 8 .%88.. .. S@. . t%
  ..;% :8 . .  . t8@@;  . 8;;:X :X X;;.t t% @;::% @  %:;;@  ;X 8;:;X.;t; :;;t. S. .:S88  t@.Xt8::: t88.. .S.t8. . t%
  . 8X;%..      ..:.: . . 8;;:S %S X;:.t ;; @;::% :. %:;;@ .%S 8;:;X .t;.:;;t  @. .:;8t   .  :.  . S88.. .. :S: . t%
 . ..;t t8. .  . 8: :S  . 8;::S S8 @t:.; @@ 8t::% 8S %::t@  X8 8;::@ S.: :;;;  ;% .:%8@    .    .  %88...:8:. ... t% 
   . SSS: ;: % . 8 :.S .. 8t;:X :X X;;.t tt @;::% @  %:;;@  ;S 8;:;X :;; :;;t .;t .:;88     .S  .. t88.. :88t%. . t%
      ;  .S.;:          . 8;::S t@ X;:.t SS @;::% 8; %::;@  t@ 8;:;X.:%t.:;;t. .. .:S8@   . :8@::  S@8....8%Xt. . t%
 . .  .   %;X;.  %888t .  8t;:S .@ X;;.;.;S @;::% @: %:;;@  .@ 8;:;X t;; :;;t      %%t%   . 88  .. :88 . :S: X: . t%
   . @%t.;XSS: . 8%:;X  . 8;::S t8 @t:.; S@ 8t:.% XS.%:;;@ .%8 8;::@ t@: :;;;   .  .  .   ..;. . .. t .  .8;:8. . t%
   . ;. 8;;  . . 8;:;S .. 8t;:X ;; X;:.t %. 8;::% 8..t::t@  t; 8;:;X .  .:;;t .  ...t.;::::::: t....@ .. .S  t: . t%
. . :%8 ;t .   . 8t::X  . 8;::S .8 X;;.t .X @;::% t: %:;;@ ..8 8;:;X .   :;;t.  :8S%t S;S.;t%;;%8S@;@ .  :;S.8: . t%
  . Xt.S;%  .  . 8t::S. . 8t;:S .  @t:.;  . 8t::% .  %::;@ .   @;:;X   . :;;t . t888%;8%8;t%;t:S88Xt@ . . S8 8... t%
  . ;% t: ..   . 8;:;S .. 8;::S . .@;;.; .  8;::t .  %:;;@ . . @;::@ .  .:;;t .  .  :t;;;;:;;;;t::. @ ..  :.;8: . t%
.  SS%::8 %X .  .8t::X  . 8t;:S .  @;:.; .. 8;::%  . %.;;@ . . 8;:;X .   ::;;     t;S%8@X8:SSSSSt . @ . .. %;%. . t%
 . ;  @.. @; . . 8%;tX . .8t:;S .. Xt;:; .. @t;;% .  %;:%@ .   8t:t@  . ..;t; . .  .: ::::::::.;   .%% .  .t:8. . t%  
 . t. ;8  @  .  .:ttt.    :tt%.    ;ttt.    ;ttt.  . .%tt;   . :ttt:     tttt      .ttttt;t;ttt. .   :    .. S:.. t%
 . ;. ;8 . .      . . . .  .  .. . .. . .  . . . .  . . . .  .  . . . ..  ..  . .   .    . .         ;. . . :t. . t%
 . %;.%8 .    . .  . X;X:.;.X @SS St@..t8; 8SS S;@. %8t 8tX ;;8; S@% @tX :t8; 8%%.    .     . . . .  :.     .;. . t%
 . . . .   . .     . @tXt@X@. S%: %88S.X @ 8X; t88%.%.% X@S X8X8. :. :8X.;X 8 8X: :%. ... . St88888X.S.      .  . t%
S@SS8.:S8@88;   .  . X@.88.;  XSXt@888:t : 8SStS88@:S. .%8XXS8St  :;. 8@8:t : 8X%%.t% %tS  .X8888StXX  . . .    . t%
%%:t.t.:;;t8S .     .tt.tt t:.%@@::XX%.@SX %X@::8%8X8@88@X8t.XXS S@X.;X@;.@SX %XX: t%.S;%.  ...StXt @. .     .  . tS
XSX:% t8:::%:.. ..   .   . .  . .  ..  ...  ... 8;;:tt8:::@. ... ... .... ... .... tS8X:;%Stt.@:% ..@.    .     . tX
::;..   ... .SSXSS .  . .   . ;@888.  .   . .  . . . . . .             .     .    .t8;t.@88%@%%S%S%%8. . .  . . . t%
88888888888888@SXSX8888888888888888888@SX%@S@t@X@..         .   .  . :8S8.@:8:@S S88@SXXXX;8SSXSXSXSXX@888888888;;;8:
        .  .  . ..  ....   ..  . . ...   ..  ..      ..X       .  8.  . . .    .     . 8   X888X     .. ..  . . . .    
"""

MARKET_OVERWRITE = """
XXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNXXXNWMWNNXKXXXXXXXXXXXNWWNXKXXXXXXXXXKXWWWWWWWWWWWWWWWWWWWWWWWWWXX
KXMMMMMMMMMMMMMMMWXXXKKKKKXNK0KXKXWMMMMMMMMMMMMMMMWNXNMMMMMMMWNWMMNXK0KKKKXXNWWNWMNKKKKNMWNWMMMNXXXXKKKXNXKKXXXNMMWNKK
XXMMMMMMMMMMMMMMMWXKK0000O0XK0KK0XWMMMMMMMMMMMMMMMMWNNMMMMMMMWNWMMMWX0KKKNWWMMWNNMWNXXXWMWNWMMMNKK00000OKK00K00NMMWNKK
KKWWMMMWWWWWWWWWWWWWWWWNNNNNNNNNNNNNNNNNNNNNWWMMMWWNXNNNNNNNNNXNNNNNWWWWWWWNWWNXNWNNNNNNNNXNWWMMMWWNNNNNWWWWWWWMMMWNXX
KKMMMMWK0KKKKKXX0KKK00XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0KKKKKXX0KKKKKXWMMMMMMMMMMMMMMMMMMXKKKKKXNMMMMMXK
XXMMMMWNNNX000KK00000OKXXXXXXXNNNNXXNNNXXXXWMMMMMMMWWWWWWWWWWWWWWWWNXKKKKKKXXKKKK00KNWWWWWWWWWWMMMMMMMMN0OOOOKWMMMMWXK
XXMMMMMMMWKOKXXXXXXKKKKKXXXXKKXXXXXXXXXKKK0KWMMMMMNXNNNNNXNWWWWWWWWWWWWWWWWWWWWWWWWWNNWWNNNNNNWWWNMMMMMMWWNXNNNNWNXNKK
XXMMMMMMMX0KNWMMMMWNWMMWWWWWWMMWNNWMMMMMMNK0XMMMMMWXKO00XNWMMMMMMWKKKXXXKKKKKNMMMMMMWWMMNOOO0NMMNNMMMMMMMWNNWWWWWNXX0K
XXMMMMMMWK0NWMMMMMX0XWMWKKKKNMMNKKWMMMMMMWNKKWMMMMNXKKKKKXWMMMMMMN0O0000OOOk0WMMMMMMNXWWXKKKXNWWNNWMMMMMMMWWNKKKKKKXKK
XXMMMMMMWNNWMMMMMMWWWMMMMMMWMMMMWWMMMMMMMMWWNWMMMMWNNNNNNNWMMMMMMWNNNNNNNNNXNMMMMMMMWNNNNNNNNNNNNNWMMMWWMWNNNXXKKKKXKK
KXMMMMMX0NMMMMXdcllllllllllllllllllll0MMMMWOooodddddddddoooddddddddddooddddddddddddoodddddddddddokNMMWOxKWNNWNWNNWNWKK
XXMMMMWOOWMMMMKc','',,,''''''''''''',kMMMMMX00kxxdxxxxxO00000000000000000Oxdxxk000000000000000000KWMMWxl0WK00KK00XWMXK
XXMMMMKkXMMMMMWXKKKKOxkkkkkkkOKKKKKKKNMMMMMMMMWNXXNNXXNWMMMMMMMMMMMMMMMMMMNXXXNMMMMMMMMMMMMMMMMMMMMMMWxl0WNXXXK00XNWKK
KXMMMNO0WMMMMMWWMMMWX0KXXXKKKXNWMMMMMWWWWMMMMMWWWWMMMMMWWWWWMMMMMMWWWWMMMMMWWWWMMMMMMWWWWMMMMMWNNWMMMWxl0MMMMWNXXXXXKK
XXMMM0ONWMMMMN0KWMW0kkKWMMMN0kkKWMMMNOkkKMMMMN0kkKWMMMWKkk0KNMMMMW0kk0WMMMMXOkOXMMMMMXOxxXMMMMXxdXMMMWxl0WMMMWNNKKKXKK
XXMMNO0NKXMMMWKXMMNOxx0WMMMNOxx0WMMMNkxxKWMMMNOxx0WMMMW0xxOKNMMMMWOxx0WMMMMXkxkXMMMMMXxll0MMMMXxdXMMMWxcOWWWWNNNWWWWKK
XXMMNOKN0XMMMN0KWMNOxx0WMMMNOxx0WMMMNkxxKWMMMNOxx0WMMMW0xxOKNMMMMWOxx0WMMMMXkxkXMMMMMXxll0WMMMWNNWMMMWxl0MMMMMMMMMMMXK
XXMMNOKNKNMMMWXXWMNOxx0WMMMNOxx0WWWMNkxxKWWWWNOxx0WMWWW0xxOKNMWWWWOxx0WMMMMXkxkXMWXNMXxll0WNXWMMMMWXNWxl0MMMMMMMMMMMXK
XXMMNOKMMMMMMN0XWMNOxx0WMMMNOxx0WX0NNkxxKWX0XNOxx0WN0XW0xxOKNMX0NWOxx0WMMMMXkxkXMXOXMXxll0WKONN0ONNOKWxl0MMMMMMMMMMMXK
XXMMNO0NXNMMMMMMMMNOxx0WMMMNOxx0WKONNkxxKWXOXNOxx0WXOKW0xxOKNMKOXNOxx0WMMMMXkxkXMX0NMXxll0WKONXolKXOKWxl0MMMMMNXNMMMXK
XXMMW0OXKKWMMMMMMMWK00XWMMMNOxx0WKONNkxxKWXOXNOxx0WNOKW0xxOKNMXOXNOxx0WMXXMXkxkXMN0XMXxll0WK0NNOONXOXWxl0MMMWW0o0MMMXK
XXMMMNO0NKKWMMMMMMWNXXNMMMMNOxx0WXONNkxxKWXONNOxx0WXOXW0xxOKNMX0NWOxx0WW00MXkxkXMN0XMXxll0WWNMMMMMWNWWxl0MMM0kOd0MMMXK
XXMMMMXkKN0XMWWMMMNOxx0WMMMNOxx0WX0NNkxxKWN0NNOxx0WN0XW0xxOKNMX0NWOxx0WWKKMXkxkXMN0NMXxll0WMMMWXXWMMMWxl0MMMOxOkKMMMXK
KXMMMMWKKWKKWKKWMMWX00XWMMMNOxx0WXONNkxxKWXOXNOxx0WNOKW0xxOKNMX0NWOxx0WM00WXkxkXMMWMMXxll0WMMMXdoKMMMWxl0MMMOx0OXMMMXK
XXMMMMMMMMKKW00MMMWNXXNMMMMNOxx0WX0NNkxxKWXOXNOxx0WN0XW0xxOKNMX0NNOxx0WW00WXkxkXMMMMMXkxxKMMMMNkxXMMMWOo0MMM0xOOKMMMXK
XXMMMMWKXWK0N00MMMNOxx0WMMMNOxx0WX0NNkxxKWX0NNOxx0WN0XW0xxOKNMX0NWOxx0WWXXMXkxkXMMMMMWWWWWMMMMMWWMMMMMNOKMMM0xOx0MMMXK
XXMMMMXkKN00WWWMMMNOxx0WMMMNOxx0WX0NNkxxKWXOXNOxx0WN0XW0xxOKNMXONWOxx0WMMMMXkxkXMMMMMMNK000000000XWMMMW0KMMMKOOd0MMMXK
XXMMMW0ONKONMMMMMMNOxx0WMMMNOxx0WXKWNkxxKWNKNNOxx0WNKNW0xxOKNMNKWWOxx0WMMMMXkxkXMMWXKK0kO00OkOOOOKKKKXN0KMMMXK0dOMMMXK
XXMMMXkKN0KWMMMMMMNOxx0WMMMNOxx0WMMMNkxxKWMMMNOxx0WMMMW0xxOKNMMMMWOxx0WMMMMXkxkXMMMNXNKkOOOOkkkkkKNXXNN0KMMMX0Od0MMMXK
XXMMW0ONKONWWWMMMMNOxx0WMMMNOxx0WMMMNOxxKWMMMNOxx0WMMMW0xxOKNMMMMWOxx0WMMMMXkxkXMMMMMN0OO0OOOkOOO0NWMMW0KMMMKOOx0MMMXK
XXMMXkKN0KMNOKMMMMNOxx0WMMMNOxx0WMMMNkxxKWMMMNOxx0WMMMW0xxkKNMMMMWOxxOWMMMMXxxkXMMMMMN0kkOOOOkkkk0NMMMWKXMMMNKOd0MMMXK
KXMMXkXX0NMNKXMMMMWNXXNMMMMWNXXNMMMMWXXXNMMMMWXXXNMMMMMNXXXNWMMMMWNXXNWMMMMWXXXWMMMMMMNXXXXXXXXXKNMMMMMWWMMMMMKx0MMMXK
XXMMXkKX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMN0XMMMXK
XXMMNKNNXWMMMMMMMMMMMMNOxxk0OONKxONNkxXW0x0WXxkNNkxXM0x0WXxokNWOxKWKxONNkkNM0x0WXxkNMMMMMMMMMMWNNWWWWWMWWMMMMMMMMMMMXK
KKNNNXWMWNXXXWMMMMMMMMNKXXKX0xKO;:0Xc,kNd,oX0;:0Xc;kNx,oX0:.;ONo,dXk,lKK:;OWd,oXO;:0WXKWN0KWMMNKKXXK0KNKXMMMMMMMMMMMXK
00KKKkKXOkk0KKNMMMMMMMNXNNKNNXWXkxKW0xONKxkXNOx0N0dxK0dx0Kkod0WKxkXXkxKNOx0WKxkXNOx0WK0WXk0WMMMMMWXKXWW0KMMMMMMMMMMMXK
MMMMMMMXKXXXKKKNK0XXXKNWX00XXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKKKXXXKKKXWMMMMMMMK0XK00XXXXWWXKNMMW0KMMMMMMMMMMMXK
K0XXXNNNNNNNNNX0000XNNNNNNNNNNNXK000XNNXKKKKKKKKNWMMMMMMMMMMMMMMMMMMMMMWXNNWNNNNWWNNNOkOkxOKKOk000000K0k0NNNNNNNNWWWXK
WNNNNNNNNNNNNNXXXXXXNNNNNNNNNNNNXXXXXX0occcccccclOWMMMMMMMMMMMMMMMMMMMMX000KKKKKKK0KXXXXXXNWWXXXXXXXXXXXXNNNNNNNNWWWWW
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:cooooc::xNMMMMMMMMMMMMMMMMMMMMNK0KK00KXK0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l::llll:::xNMMMMMMMMMMMMMMMMMMMMNK0KKKKKKK00XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
