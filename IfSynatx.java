import java.util.Scanner;
public class BlockSynatax{

	public static boolean checkStartAppearance(String str,String s){
		//IF
		int count=0;
		if(s.equals("0")){
			count=0;
			if(str.charAt(0)=='i' && str.charAt(1)=='f' && str.charAt(2)=='('){
				count++;;
			}
		}

		//{ after condition (
		if(s.equals("1")){
			int startPos=str.indexOf(')');	
			if(str.charAt(startPos+1)=='{'){
				count++;
			}
			
		}
		
		if(s.equals("2")){
			int startPos=str.indexOf('}');
			if(str.charAt(startPos+1)=='e' && str.charAt(startPos+2)=='l' && str.charAt(startPos+3)=='s' 
			&& str.charAt(startPos+4)=='e'){
				count++;
			}
		}

		if(count==1){
			return true;
		}
		else{
			return false;
		}
		
	}

	public static boolean checkAppearance(String str,char ch){
		int startPos;
		int endPos;
		int count=0;
		if(ch==')'){
			startPos=str.indexOf('(');
			endPos=str.indexOf(ch);
			count=0;
			for(int i=startPos;i<endPos;i++){
				if(str.charAt(i)=='(' || str.charAt(i)==')'){
					count++;
				}
			}
		}

		if(ch=='}'){
			startPos=str.indexOf('{');
			endPos=str.indexOf(ch);
			count=0;
			for(int i=startPos;i<endPos;i++){
				if(str.charAt(i)=='{' || str.charAt(i)=='}'){
					count++;
				}
			}
		}

		if(count==1){
			return true;
		}
		else{
			return false;
		}
	}

	public static boolean checkIfElseSyntax(String str){
		int count=0;
		if(checkStartAppearance(str,"0")==true){
			count=0;
			if(checkAppearance(str,')')==true){
				count=0;
				if(checkStartAppearance(str,"1")==true){
					count=0;
					if(checkAppearance(str,'}')==true){
						count=0;
						if(checkStartAppearance(str,"1")==true){
							count=0;
							if(checkAppearance(str,')')==true){
								count++;
							}
						}
					}
				}
			}
		}
		if(count==1){
			return true;
		}
		else{
			return false;
		}
		
	}

	public static void main(String[] args){
		String str= new Scanner(System.in).next();
		if(checkIfElseSyntax(str)==true){
			System.out.println("Synatx is correct");
		}
		else{
			System.out.println("Synatx is incorrect");
		}
	}
}