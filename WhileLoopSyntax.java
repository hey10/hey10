import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class WhileLoopSyntax{

	public static boolean checkFollowingCharacter(String str, char ch1,char ch2){
		return (str.charAt(str.indexOf(ch1)+1)==ch2)?true:false;		
	}

	public static boolean checkSyntax(String str, char ch1,char ch2){
		int count=0;
		for(int i=str.indexOf(ch1)+1;i<str.indexOf(ch2);i++)
			if(str.charAt(i)=='(' || str.charAt(i)==')' || str.charAt(i)=='{' || str.charAt(i)=='}')
				count++;
		
		return (count==0)?true:false;
		
	}
	
	public static boolean checkBraces(String str){
		int count1=0,count2=0;
		char[] ch=str.toCharArray();
		for(char c:ch){
			if(c=='{')
				count1++;
			if(c=='}')
				count2++;
		}
		
		return (count1==count2)?true:false;
	}
	
	public static boolean checkWhileLoopSyntax(String str){
		boolean status=false;
		if(checkFollowingCharacter(str,'e','(')==true){
			if(checkSyntax(str,'(',')')==true){
				if(checkFollowingCharacter(str,')','{')==true){
					if(checkBraces(str)==true){
						status=true;
					}
					else
						status=false;
				}
				else
					status=false;
			}
			else
				status=false;
		}
		else
			status=false;
		return status;
	}
	

	public static void main(String[] args) throws Exception{
		System.out.println("Enter the While Loop Statement=");

		List<String> tokens = new ArrayList<>();
            	Scanner lineScanner = new Scanner(System.in);

		while(lineScanner.hasNext()){
			String s=lineScanner.next();
			if(s.equals("\n"))
				break;
			tokens.add(s);
		}

		String str=String.join(",",tokens);		

		if(checkWhileLoopSyntax(new String(str))==true)
			System.out.println("Valid While Loop Statement");
		else
			System.out.println("Invalid While Loop Statement");
	}
}