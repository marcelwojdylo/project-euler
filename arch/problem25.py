fibonaccis = open("fibonaccis","r")
index = 0
for line in fibonaccis:
    index += 1

print(len("1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816"))
print(len("661337322839244020529448762061498838625822185407709121508540998594682904585308540198620399347330470400653280666540992810413273565832926917994398713638718230004471776413151146318909185589434770973461837586080318941036906375808818987789429626217366616261579890860369055555894732519548901040157604298546742957666096845809463021127999592568557636384690462092341124092401245911116667639704650585763476554594656814646920798543755041993472555505701157143290739289844688760895075749533130953287080934600205342326904398216342904642143410026582439596278979961166556037913414174756579068802168337413360918567937945101952123966744780579475400056938418442029794142856905251486526028946063939727834195575354173400454719814829506586601492013100468780852140836021109820860257494909387619656513364393990237289782342713423952649505274336811640790273740875206602634583227097792146230883268422965993230492657630338344967767776216497296016612316692840479306680187737608910337658122657075262622220319456797676633847360981"))
print(index)

# def nextFib(a,b):
#     return a+b
# fibonaccis = open("fibonaccis", "w")
# a = 1
# fibonaccis.write(str(a)+"\n")
# fibonaccis.write(str(a)+"\n")
# b = 2
# fibonaccis.write(str(b)+"\n")
# while (len(str(b)) < 1000):
#     c = nextFib(a,b)
#     fibonaccis.write(str(c)+"\n")
#     a = b
#     b = c

