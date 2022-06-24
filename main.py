import FormulaParse

if __name__ == "__main__":
    input_formula_001 = """=IF(A1<10,SUM(B2:B10),100-MAX(10,B11))"""
    input_formula_002 = """=SUM(A2:A5)+SUM(test2!A3:A5)"""
    input_formula_003 = """=SUM(A1:A5,SUM(A6:A8))"""
    input_formula_004 = """=IF(A1<10,SUM(B2:B10),100-MAX(10,B11))"""
    input_formula_005 = """=VLOOKUP(E2,'Exchange Rate'!$B$3:$C$15,2,FALSE)"""
    input_formula_006 = """=IF(SUM(C1:C10) > SUM(D1:D10), SUM(C1:C10), SUM(D1:D10))"""
    input_formula_007 = """=-SUMIFS('Trial Balance'!$J:$J,'Trial Balance'!$K:$K,Liquidity!$A13,'Trial Balance'!$L:$L,Liquidity!B$1)/1000"""
    input_formula_008 = """=IF(AND(A2<>0, (1/A2)>0.5),"Good", "Bad")"""
    input_formula_009 = """=IF(A2<>0, IF((1/A2)>0.5, "Good", "Bad"), "Bad")"""
    input_formula_0010 = """=IF(A1<A2,10,20)"""
    input_formula_0011 = """=SUM(IF(A1<A2,10,20),IF(A3<A4,10,20))"""
    input_formula_0012 = """=IF(A1<A2,SUM(A1,A2),SUM(A3,A4))"""
    input_formula_0013 = """=IF(SUM(A1,A2)<SUM(A3,A4),10,20)"""
    input_formula_0014 = """=IF(IF(A1<A2,10,20)<10,10,20)"""
    input_formula = input_formula_004

    output = FormulaParse.get_formula_token_list(input_formula)
    print(output)
